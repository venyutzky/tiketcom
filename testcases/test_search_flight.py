# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import pytest
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",".."))
# from webdriver_manager.chrome import ChromeDriverManager
from tiketcom.pages.HomePage import HomePage
from tiketcom.pages.SearchFlightPage import SearchFlightPage
from tiketcom.pages.FlightSearchResultPage import FlightSearchResultPage


@pytest.mark.usefixtures("setup")
class TestSearchFlight():
    
    def test_search_flight(self):
        
        # setup
        
        # click plane icon
        in_homepage = HomePage(self.driver, self.wait)
        in_homepage.click_plane_icon()
        in_homepage.page_scroll()
        
        # choose flight type
        in_searchflightpage = SearchFlightPage(self.driver, self.wait)
        in_searchflightpage.select_flight_type()

        # select going from location
        in_searchflightpage.select_depart_from("Jakarta")

        
        # select going to location
        in_searchflightpage.select_going_to("Padang")
        
        # select date
        in_searchflightpage.select_depart_date("Choose Sabtu, 11 Februari 2023 as your check-in date. It’s available.")
        
        # Provide passenger number
        in_searchflightpage.select_number_of_passenger()
        
        # Provide cabin type
        in_searchflightpage.select_cabin_type()

        # click on SELESAI button
        in_searchflightpage.click_selesai_button()
        
        # click on flight search button
        in_searchflightpage.click_search_flight_button()
        
        # click on pop up card
        in_flightsearchresult_page = FlightSearchResultPage(self.driver, self.wait)
        in_flightsearchresult_page.click_popup()
        # self.driver.find_element(By.XPATH, "//div[@class='comp-info-box']//div[@class='v3-btn v3-btn__blue list-horizontal__middle btn-action']").click()
        # time.sleep(1)
        
        # scroll down page
        in_flightsearchresult_page.page_scroll()
        # pageLength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        # match =  False
        # while (match == False):
        #     lastCount = pageLength
        #     time.sleep(1)
        #     pageLength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        #     if lastCount == pageLength:
        #         match = True
                           
        # time.sleep(4)
        

        