from bs4 import BeautifulSoup
import urllib


class base_online_scraper(object):

    """Class Definition for an online scraper.
    The base_online_scraper scrapes 1 page of course data from a webpage.

    url: a String representing the webpage that this is going to scrape.
    """

    def __init__(self, url):
        """Inits an instance of base_online_scraper

        Args:
            url: A string representing the webpage that is to be scraped.

        Returns:
            An instance of base_online_scraper with the url as *url*.
        """

        self.url = url

    def __setup(self):
        """ Sets up the scraper by first opening up the url, parsing the HTML,
        and then returning a parsed portion of the HTML containing the course
        information

        Returns:
            A portion of the HTML that is semi parsed, containing all
            information about the courses on that particular page.
            Returned as a list of tags (bs4.element.tag)
        """

        fp = urllib.urlopen(self.url)
        soup = BeautifulSoup(fp, 'lxml')
        course_block = soup.find_all('div', class_="courseblock")
        return course_block

    def scrape(self):
        """Calls the __setup function to obtain all course information on the page,
        and then parses the data for each courses individual data, including
        course code, course name, credits and course description.
        """

        course_block = self.__setup()
        for course in course_block:
            # Scrape information from each course block
            courseCode, courseName, credits = course.find(
                                              'p',
                                              class_="courseblocktitle"
                                              ).text.split(".", 2)
            courseDesc = course.find('p', class_="courseblockdesc").text

            # Clean up Strings
            courseCode.strip()
            courseId = courseCode[-4:]
            courseType = courseCode[:-5]
            courseName = courseName[2:]
            credits.strip(" .")
            courseDesc.strip()

            # Return Data as Dictionary
            # [courseCode, courseName, credits, courseDesc]
            returnList = [courseCode, courseName, credits, courseDesc]
            return returnList
