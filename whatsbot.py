from selenium import webdriver
import time
import os

class WhatsappBot:
    def __init__(self):
        self.dir_path = os.getcwd()
        self.chrome = self.dir_path+'/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"user-data-dir="+self.dir_path+"/profile/wpp")
        self.driver = webdriver.Chrome(self.chrome, chrome_options=self.options)
        self.driver.get('https://web.whatsapp.com')
        while len(self.driver.find_elements_by_id('side')) < 1:
            time.sleep(1)
        grupo = self.driver.find_element_by_xpath('//span[@title="Bolao teste"]')
        grupo.click()
        time.sleep(3)

    def EnviarMensagens(self):
        chat_box = self.driver.find_element_by_class_name('p3_M1')
        chat_box.click()
        time.sleep(3)
        chat_box.send_keys('teste_bot')
        botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
        botao_enviar.click()
        time.sleep(3)

    def EscutaMensagens(self):
        post = self.driver.find_elements_by_class_name('_22Msk')
        ultimo_post = len(post) -1
        #cabecalho = post[ultimo_post].find_element_by_xpath('.//span[@dir="auto"]').text
        infos = post[ultimo_post].find_element_by_xpath('.//div[contains(@class, "copyable-text")]')
        hora_envio_msg = infos.get_attribute('data-pre-plain-text')[1:6]
        data_envio_msg = infos.get_attribute('data-pre-plain-text')[8:18]
        autor_envio_msg = infos.get_attribute('data-pre-plain-text')[20:-2]
        msg_recebida = post[ultimo_post].find_element_by_css_selector('span.selectable-text').text
        return hora_envio_msg, data_envio_msg, autor_envio_msg, msg_recebida