from bs4 import BeautifulSoup as bs
from src.adapters.indeed_adapter import *
import pdb

html_doc = """
<td class="resultContent"><div class="css-1m4cuuf e37uo190"><h2 class="jobTitle css-1h4a4n5 eu4oa1w0" tabindex="-1"><a aria-label="full details of Senior Data Center Infrastructure Engineer" class="jcs-JobTitle css-jspxzf eu4oa1w0" data-ci="375541361" data-empn="933222862051587" data-hide-spinner="true" data-hiring-event="false" data-jk="074427a3c9bee221" data-mobtk="1h03oa9nr2i9c001" href="/pagead/clk?mo=r&amp;ad=-6NYlbfkN0C56rqW-QaaSzPxgC8-7DVr9-xTwNQ8D0EnYbiS4Uxm2apKzX-Bw0NjSYZusKxg0sDfdxzaaHj3HalGY6KpliOAohX5yPpvfpNjPTo4tVkxtihBaxKkaXJWqdW9I1-6JazpZEQCTOLawPBS1Ck5D42Aj8xqXEtQajyj3mb552TXyxA06m7pHVcsVDnLuEA0VSfwaskLYAo8IuAyjLixJLT4YxfcVtxAZ0r88PV143Fz-r_LEKe4BWnNm8KQyU_37oTnVTZa1pJrKM3vaz-8-V4HmZNr9pa_zzWLlIGtJwAZ5jnM1hvbHnstKf2EHja55hK3aCqiQimISOCyM_IU1uPLoc9p4OriXqIRne1Lbr839f_GYD_SeBWyGnk_B3CA8G-e_blR2SphShM-ysgGuxKYBrNm6VfpQG5z6G5Qhg5l_yeNv1yQ4gF13CEVLD4tO2NqKc5oEOrYG03hxV8SV70DzXLR6O8Xt8nEvV44pSH0YjqET0qcnz7vXQiCIa-vtKPsBmqrE9A_BQO7ah6lzwD4y_Gsds7VPqd3FN92TlaAW246RjCxkgg8CIoSTLYF9cXMHFmr5CScrTCpkAYS0ExKO7RrwxsMVHo=&amp;xkcb=SoD5-_M3PD4m4ZQ9QR0KbzkdCdPP&amp;p=0&amp;fvj=0&amp;vjs=3" id="sj_074427a3c9bee221" role="button" target="_blank"><span id="jobTitle-074427a3c9bee221" title="Senior Data Center Infrastructure Engineer">Senior Data Center Infrastructure Engineer</span></a></h2></div><div class="heading6 company_location tapItem-gutter companyInfo"><span class="companyName">MJHS</span><span aria-hidden="true" class="ratingsDisplay withRatingLink"><span aria-label="3.6 out of five stars rating" class="ratingNumber" role="img"><span aria-hidden="true">3.6</span><svg aria-hidden="true" class="starIcon" fill="none" height="12" role="presentation" viewbox="0 0 16 16" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M8 12.8709L12.4542 15.5593C12.7807 15.7563 13.1835 15.4636 13.0968 15.0922L11.9148 10.0254L15.8505 6.61581C16.1388 6.36608 15.9847 5.89257 15.6047 5.86033L10.423 5.42072L8.39696 0.640342C8.24839 0.289808 7.7516 0.289808 7.60303 0.640341L5.57696 5.42072L0.395297 5.86033C0.015274 5.89257 -0.13882 6.36608 0.149443 6.61581L4.0852 10.0254L2.90318 15.0922C2.81653 15.4636 3.21932 15.7563 3.54584 15.5593L8 12.8709Z" fill="#767676"></path></svg></span></span><div class="companyLocation">Brooklyn, NY 11220<!-- --> <span class="companyLocation--extras">(<!-- -->Sunset Park area<!-- -->)</span><span class="more_loc_container"><a aria-label="Same Senior Data Center Infrastructure Engineer job in 1 other location" class="more_loc" href="/addlLoc/redirect?tk=1h03oa9nr2i9c001&amp;jk=074427a3c9bee221&amp;dest=%2Fjobs%3Fq%3Ddata%2Bengineer%26l%3DNew%2BYork%252C%2BNY%26grpKey%3D8gcGdG5mdGNsuA-d6BqqECQKCW5vcm10aXRsZRoXaW5mcmFzdHJ1Y3R1cmUgZW5naW5lZXI%253D" rel="nofollow">+1 location</a></span></div></div><div class="heading6 tapItem-gutter metadataContainer noJEMChips salaryOnly"><div class="metadata estimated-salary-container"><span class="estimated-salary"><svg aria-hidden="true" aria-label="Estimated $89.1K to $113K a year" fill="none" role="presentation" viewbox="0 0 16 13" xmlns="http://www.w3.org/2000/svg"><defs></defs><path clip-rule="evenodd" d="M2.45168 6.10292c-.30177-.125-.62509-.18964-.95168-.1903V4.08678c.32693-.00053.6506-.06518.95267-.1903.30331-.12564.57891-.30979.81105-.54193.23215-.23215.4163-.50775.54194-.81106.12524-.30237.18989-.62638.19029-.95365H9.0902c0 .3283.06466.65339.1903.9567.12564.30331.30978.57891.54193.81106.23217.23215.50777.41629.81107.54193.3032.12558.6281.19024.9562.1903v1.83556c-.3242.00155-.6451.06616-.9448.19028-.3033.12563-.5789.30978-.81102.54193-.23215.23214-.4163.50774-.54193.81106-.12332.2977-.18789.61638-.19024.93849H3.99496c-.00071-.32645-.06535-.64961-.19029-.95124-.12564-.30332-.30979-.57891-.54193-.81106-.23215-.23215-.50775-.4163-.81106-.54193zM0 .589843C0 .313701.223858.0898438.5.0898438h12.0897c.2762 0 .5.2238572.5.5000002V9.40715c0 .27614-.2238.5-.5.5H.5c-.276143 0-.5-.22386-.5-.5V.589843zM6.54427 6.99849c1.10457 0 2-.89543 2-2s-.89543-2-2-2-2 .89543-2 2 .89543 2 2 2zm8.05523-2.69917v7.10958H2.75977c-.27615 0-.5.2238-.5.5v.5c0 .2761.22385.5.5.5H15.422c.4419 0 .6775-.2211.6775-.6629V4.29932c0-.27615-.2239-.5-.5-.5h-.5c-.2761 0-.5.22385-.5.5z" fill="#595959" fill-rule="evenodd"></path></svg><span>Estimated $89.1K - $113K a year</span><button aria-haspopup="true" aria-label="About Indeed's estimated salaries" class="estimated-salary-legal-disclaimer-button" type="button"><img alt="" aria-hidden="true" class="estimated-salary-legal-disclaimer-icon" src="https://c03.s3.indeed.com/mosaic-provider-jobcards/dist/QuestionCircle.90151952809f3707396c.svg"/></button></span></div><div class="metadata"><div class="attribute_snippet" data-testid="attribute_snippet_testid"><svg aria-hidden="true" aria-label="Job type" fill="none" height="13" role="presentation" viewbox="0 0 14 13" width="14" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M4.50226.5c-.27614 0-.5.223858-.5.5v2.1H.5c-.276142 0-.5.22386-.5.5v1.9h14V3.6c0-.27614-.2239-.5-.5-.5h-3.4977V1c0-.276142-.22389-.5-.50004-.5h-5Zm4.19962 2.6H5.30344V1.8h3.39844v1.3Z" fill="#595959" fill-rule="evenodd"></path><path d="M5.70117 6.80005H0v5.20005c0 .2761.223857.5.5.5h13c.2761 0 .5-.2239.5-.5V6.80005H8.30117v.80322c0 .27614-.22386.5-.5.5h-1.6c-.27614 0-.5-.22386-.5-.5v-.80322Z" fill="#595959"></path></svg>Full-time</div></div></div><div class="heading6 error-text tapItem-gutter"></div></td>
"""
html_doc = bs(html_doc, 'html.parser')
card = html_doc.find('td')


def test_get_id_gets_id():
    indeed_adapter = IndeedAdapter(card)
    id = indeed_adapter.get_id()
    assert id == "074427a3c9bee221"

def test_get_title():
    indeed_adapter = IndeedAdapter(card)
    assert indeed_adapter.get_title() == "Senior Data Center Infrastructure Engineer"

def test_get_company_name():
    indeed_adapter = IndeedAdapter(card)
    assert indeed_adapter.get_company_name() == "MJHS"

def test_get_city_state():
    indeed_adapter = IndeedAdapter(card)
    city, state = indeed_adapter.get_city_state()
    assert city == 'Brooklyn'
    assert state == 'NY'

def test_get_salary_text():
    indeed_adapter = IndeedAdapter(card)
    assert indeed_adapter.get_salary_text() == 'Estimated $89.1K - $113K a yearFull-time'

def test_clean_salaries_turns_the_text_with_k_into_thousands():
    salary_text = 'Estimated $89.1K'
    indeed_adapter = IndeedAdapter(card)
    indeed_adapter.clean_salary(salary_text)

def test_clean_salary_returns_none_when_not_passed_numeric_values():
    salary_text = 'Estimated '
    indeed_adapter = IndeedAdapter(card)
    assert indeed_adapter.clean_salary(salary_text) == None
    
def test_clean_salaries_returns_multiple_salaries_if_multiple_are_provided():
    salary_text = 'Estimated $89.1K - $113K a yearFull-time'
    indeed_adapter = IndeedAdapter(card)
    assert indeed_adapter.clean_salaries(salary_text) == [89_100.0, 113_000.0]



def test_run_adapter_returns_instance_of_position():
    indeed_adapter = IndeedAdapter(card)
    position = indeed_adapter.run()
    assert type(position) == Position

def test_run_adapter_returns_obj_with_correct_attributes():
    indeed_adapter = IndeedAdapter(card)
    position = indeed_adapter.run()
    obj_keys = ['id', 'title', 'min_salary', 'max_salary', 'city', 'state', 'company_name']
    keys = list(vars(position).keys())
    assert obj_keys == keys

def test_run_adapter_returns_obj_with_correct_values():
    indeed_adapter = IndeedAdapter(card)
    position = indeed_adapter.run()
    obj_vals = ['074427a3c9bee221', 'Senior Data Center Infrastructure Engineer', 89100.0, 113000.0, 'MJHS', 'Brooklyn', 'NY']
    vals = list(vars(position).values())
    assert obj_vals == vals