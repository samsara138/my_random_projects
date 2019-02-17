#special packages:lxml,BeautifulSoup
import bs4 as bs
import urllib.request
import time

#scrap the fifth paragraph from uvic's html
def init_scrapper():
    sauce = urllib.request.urlopen("https://www.uvic.ca/").read()
    soup = bs.BeautifulSoup(sauce,"lxml")
    p = soup.find_all('p')
    return str(p[4].text)

#see if UVIC is open or not
def text_analyse(web_info):
    sample = "The university anticipates campus will be open Friday, Feb. 15. We are monitoring conditions and will confirm tomorrow morning by 6:30 a.m."
    if(web_info == sample):
        return True
    else:
        return False

#output to user according to campus' status
def output(open):
    if (open):
        print("UVIC is still open")
    else:
        print("FUCKING PARTYYYYYY!!!!!")

def main():
    print("start of program",'\n')
    info = init_scrapper()
    open = text_analyse(info)
    while True:
        output(open)
        time.sleep(2)

if __name__ == "__main__":
    main()
