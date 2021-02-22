# Login to https://www.toptal.com/
# Verify you are the Home Page of https://www.toptal.com/
# Search for Start Hiring Button and Click on it
# use word=python
# test 1 follow all the above steps and type in a Skill and click on a desired on
# test 2 follow all the above steps and choose a Predifined Skill and click on a desired on
# check if the Next Button is disabled with No Skill selected
# check if the Skip Button is enabled with no Skill selected
# Verify Skill Page with Header Text (What skills would you like to see in your new hire?)
# Skip the Desired Skill Page without entering or selecting a skill
# Skip the Desired Skill Page with entering or selecting a skill
# Verify Selected Skill with Presence of element displayed using btn_SelectedSkill_xpath locator
# Verify Contact Page at the end of the Questions
# Verify if Connect Me With Talent Button is disabled when Contact form is empty
# Verify if Connect Me With Talent Button is disabled when Contact form is not empty
# Verify if Connect Me With Talent Button is disabled when Contact form is half filled
import pytest
from PageObjects.developer import HireDeveloper
from Tests.setup import SetUp

class TestTopTalDeveloperPage:
    global url,skill
    skill = "Python"
    browser = SetUp.browser

    def test_verify_home_page(self,browser):
        self.dev = HireDeveloper(browser)
        self.dev.verifyHomePage()

    def test_verify_Question_Page(self, browser):
        self.dev = HireDeveloper(browser)
        self.dev.clickHireTopTalent()
        self.dev.verifyDevQuestionPage()



