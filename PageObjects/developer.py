from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from Tests.setup import SetUp
from time import sleep
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains


class HireDeveloper:
    # Home Page Locators
    #############################################################
    # Locator Descriptions
    # rad-radio button
    # lnk-link
    # btn-button
    # txtbox
    #
    #############################################################
    btn_StartHiring_linktext = "Start Hiring"
    btn_GetStarted_xpath = "//button[@id='save_new_company_create_lead']"
    btn_Next_xpath = "//button[@class='step-submit button has-chevron']"  # same on every page
    btn_HireTopTalent_xpath = "//a[@class='_1bcYCljm _2u-I7BW0 _3McSaz1R  _2716rq5F ']"
    rad_Developers_xpath = "//input[@id='interested_in_developers']"
    rad_ProjectHiringFor_css = "//input[@id='option_already_working']"
    rad_Product_Specification_xpath = "//input[@id='option_rough_idea']"
    rad_HowLongDoYouNeedDeveloper_xpath = "//input[@value='longer_than_6_months']"
    rad_HowManyDevsNeeded_xpath = "//input[@id='option_multiple']"
    rad_LevelOfTimeCommitment_xpath = "//input[@id='option_full_time']"
    txtbox_DesiredSkill_css = "[placeholder='Desired areas of expertise (e.g., JavaScript, Ruby, etc.)']"
    btn_Skip_xpath = "//button[@class='step-skip button is-white']"
    btn_SelectedSkill_xpath = "//span[@class='skills_selector-item_text']"
    rad_NumberOfEmployees_xpath = "//input[@value='between_51_and_200']"
    rad_WhenDeveloperStarts_xpath = "//input[@id='option_immediately']"
    rad_RemoteDev_xpath = "//input[@id='option_yes']"
    rad_FeeAgreement_xpath = "//input[@id='option_yes']"
    txtbox_Email_xpath = "//input[@name='email']"
    txtbox_CompanyNmae_xpath = "//input[@name='company_name']"
    txtbox_ContactName_xpath = "//input[@name='contact_name']"
    msg_DevPageMessage_css = "div.message_box-details > div"
    rad_HiddenLocator_xpath = "//div[@class='radio is-selected']"
    #Other Variables
    web_url = "https://www.toptal.com/"
    dev_page_msg = "Thanks for your interest in hiring through Toptal! Before we get started, we’d like to ask a few questions to better understand your business needs."
    home_page_title = "Toptal - Hire Freelance Talent from the Top 3%"



    def __init__(self,driver):
        self.driver = driver
        wait = WebDriverWait(driver,15)


    def clickGetStarted(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.btn_GetStarted_xpath).click()

    def verifyHomePage(self):
        browser = self.driver
        url = browser.current_url
        if url == self.web_url:
            assert self.home_page_title in browser.title
        else:
            assert False


    def verifyDevQuestionPage(self):
        browser = self.driver
        msg = browser.find_element(By.CSS_SELECTOR,self.msg_DevPageMessage_css).text
        assert self.dev_page_msg in msg
        return True

    def setDeveloperRole(self):
        browser = self.driver
        dev_rad = browser.find_element(By.XPATH,self.rad_Developers_xpath)
        hid_rad = browser.find_element(By.XPATH, self.rad_HiddenLocator_xpath)
        action = self.action
        action.move_to_element(dev_rad).click(hid_rad).perform()



    def clickHireTopTalent(self):
        browser = self.driver
        browser.find_element(By.XPATH, self.btn_HireTopTalent_xpath).click()


    def setProjectType(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.rad_ProjectHiringFor_xpath).click()

    def clickNext(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.btn_Next_xpath).click()

    def setProductSpecification(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.rad_Product_Specification_xpath).click()

    def setDevelopersNeeded(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.rad_HowManyDevsNeeded_xpath).click()

    def setLevelOfCommitment(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.rad_LevelOfTimeCommitment_xpath).click()

    def setSkillsNeeded(self,skill):
        browser = self.driver
        search = browser.find_element(By.CSS_SELECTOR,self.txtbox_DesiredSkill_css).send_keys(skill)
        search.send_keys(Keys.RETURN)

    def setEmployees(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.rad_NumberOfEmployees_xpath).click()

    def setStartTime(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.rad_WhenDeveloperStarts_xpath).click()

    def setRemoteWorkStatus(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.rad_RemoteDev_xpath).click()

    def setHourlyRate(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.rad_FeeAgreement_xpath).click()

    # def verifyContackPage(self):
    #     browser = self.driver  # create action chain object
    # action = ActionChains(driver)









