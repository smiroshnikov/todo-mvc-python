# -*- coding: utf-8 -*-

# the sexy thing about this that it supports Cyrrilic
#This is tested feature name
Feature: Checking yandex search search
#Scenario Name unique ? Will test tomorrow
  Scenario: Сheck yandex empty search result
  # steps
    Given website "ya.ru"
    Then push button with text 'Найти'
    Then page includes text 'Задан пустой поисковый запрос'

  Scenario: Сheck yandex full search result (expect to fail)
    Given website "ya.ru"
    Then push button with text 'Найти'
    Then page includes text 'Задан пустой поисковый запрос'