#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""      
    Documento de integração Python Active Campaign API
    
    Cria um usuário no active campaign, insere ele em uma lista e insere duas tags

    #insert_contact
    
    Realiza a inserção de um contato dentro do Active Campaign

    #insert_contact_in_list

    Realizar a inserção do contato criado em uma lista

    #insert_tag_contact

    Realiza a inserção de duas Tags em um único contato.
         
    #use sem moderação!
"""
 
__author__ = "Ricardo Sousa"
__copyright__ = "Free"
__credits__ = "Ricardo De Maria Sousa"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ricardo Sousa"
__email__ = "ricardo.dmsousa@gmail.com"
__status__ = "Production"


import json
import urllib.parse
import urllib.request
import requests
from datetime import datetime
import re

class Contact:
    """ Configuração do token e urls de envio post. """
    
    def __init__(self):
        now = datetime.now()
        self.date_now = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
        self.url_contact = 'https://active.api-us1.com/api/3/contact/sync'
        self.url_list_active_contact  = 'https://active.api-us1.com/api/3/contactLists'
        self.url_tag_active = 'https://active.api-us1.com/api/3/contactTags'
        self.header_secret = {'Api-Token':'TOKEN'}
        self.return_request = requests.post(self.url_contact, headers=self.header_secret)
    
    """ Inserindo um contato no active campaign . """

    def insert_contact(self, email, firstname, phone):
        if self.return_request != 404:
            data_contact = {'contact':{'cdate':str(self.date_now), 'email':email, 'firstName':firstname, 'phone':phone}}
            return_insert_contact = requests.post(self.url_contact, headers=self.header_secret, json=data_contact)
            return_insert_contact_json = return_insert_contact.json()
            self.id_contact = return_insert_contact_json['contact']['id']
            self.return_status_code = return_insert_contact.status_code
            return self.id_contact

    """ Inserindo o usuário criado em uma lista. """

    def insert_contact_in_list(self, id):
        if self.return_status_code == 200:
            insert_list_active = {"contactList": {'list': 'ID_LIST','contact': str(id),'status': '1'}}
            return_list_insert_active = requests.post(self.url_list_active_contact, headers=self.header_secret, json=insert_list_active)
            self.return_insert_list_contact = return_list_insert_active.status_code
   
    """ Inserindo tag ao usuário criado. """
   
    def insert_tag_contact(self):
        if self.return_status_code == 200:
            id_contact = self.id_contact
            insert_first_tag = {"contactTag": {"contact": str(id_contact),"tag": "ID_TAG"}} 
            insert_second_tag = {"contactTag": {"contact": str(id_contact),"tag": "ID_TAG"}}
            return_insert_first_tag = requests.post(self.url_tag_active, headers=self.header_secret, json=insert_first_tag)
            if return_insert_first_tag.status_code == 200:
                return_second_tag = requests.post(self.url_tag_active, headers=self.header_secret, json=insert_second_tag)
