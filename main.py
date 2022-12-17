import requests
import bs4

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"
}

job_titles = []
company_name = []
company_location = []
type_job = []
space = []
links = []
page_num = 0

while True:
    result = requests.get(f"https://wuzzuf.net/search/jobs/?a=spbg&q=illustrator&start=0{page_num}",headers=headers)

    soup = bs4.BeautifulSoup(result.content, "html.parser")

    job_titles = soup.find_all("h2", {"class":"css-m604qf"})
    company_name = soup.find_all("a", {"class": "css-17s97q8"})
    company_location = soup.find_all("span",{"class":"css-5wys0k"})
    type_job = soup.find_all("span",{"class":"css-1ve4b75 eoyjyou0"})

    for i in range(len(job_titles)):
        job_titles.append(print("job_titles : " + job_titles[i].text))
        company_name.append(print("company_name : " + company_name[i].text))
        company_location.append(print("company_location : " + company_location[i].text))
        type_job.append(print("type_job : " + type_job[i].text))
        space.append(print("****************************************************************"))
    page_num +=1
    if page_num >= 14:
        break

