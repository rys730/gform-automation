import os
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

GFORM_URL= os.getenv("GFORM_URL")

# use selenium manager
def setup_web_driver():
    driver = webdriver.Firefox()
    return driver

def radio_question(driver, params: str):
    form = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[contains(@data-params, '{params}')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", form)
    radio_buttons = form.find_elements(by=By.XPATH, value=".//div[@role='radio']")
    selected_gender = random.choice(radio_buttons)
    selected_gender.click()
    return

def radio_question_fixed_answer(driver, params: str, answer_index: int):
    form = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[contains(@data-params, '{params}')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", form)
    buttons = WebDriverWait(form, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, ".//div[@role='radio']"))  # Adjust the XPath as necessary
    )

    button_to_click = buttons[answer_index-1]
    driver.execute_script("arguments[0].scrollIntoView(true);", button_to_click)
    button_to_click.click()
    return

def text_question(driver, params: str, answer: str):
    form = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[contains(@data-params, '{params}')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", form)
    input_form = form.find_element(by=By.XPATH, value=".//input")
    input_form.click()
    input_form.send_keys(answer)
    return

def next_page_button(driver, text: str = "Berikutnya"):
    next_button = driver.find_element(By.XPATH, f"//span[text()='{text}']/ancestor::div[@role='button']")
    next_button.click()
    return

def main():
    try:
        driver = setup_web_driver()
        driver.get(GFROM_URL)

        radio_question_fixed_answer(driver, "1676635795", 0)
        next_page_button(driver)

        name = ''.join(random.choices(string.ascii_uppercase, k=2))
        text_question(driver, "Inisial Nama", name)
        radio_question(driver, "jenis kelamin")

        random_age = str(random.randint(20, 24))
        text_question(driver, "Usia", random_age)
        radio_question_fixed_answer(driver, "Fakultas", 6)
        text_question(driver, "Jurusan / Program studi", "Teknik Informatika")
        radio_question(driver, "Apakah Saudara pernah mengikuti program magang ?")
        radio_question(driver, "Apakah Saudara pernah mengikuti pelatihan/ seminat terkait dengan karir ?")
        radio_question(driver, "Apakah Saudara telah mengetahui karir seperti apa yang Saudara inginkan ?")
        next_page_button(driver)

        radio_question(driver, "Orang tua menggunakan hukuman fisik untuk mendisiplin saya")
        radio_question(driver, "Orang tua memukul saya jika saya tidak patuh")
        radio_question(driver, "Orang tua menampar saya ketika saya berperilaku buruk")
        radio_question(driver, "Orang tua mencengkeram saya saat saya tidak patuh")
        radio_question(driver, "Orang tua membentak ketika saya berperilaku buruk")
        radio_question(driver, "Orang tua menegur agar saya menjadi lebih baik")
        radio_question(driver, "Orang tua saya menghukum dengan cara tidak memberikan saya uang sakut lagi")
        radio_question(driver, "Orang tua menggunakan ancaman sebagai hukuman tanpa memberikan penjelasan")
        radio_question(driver, "Orang tua menghukum dengan melarang saya untuk keluar pada akhir pekan")
        radio_question(driver, "Ketika saya bertanya kepada orang tua mengapa saya harus melakukan sesuatu hal, jawaban yang diberikan biasanya karena saya orang tuamu dan saya ingin kamu melakukannnya")
        radio_question(driver, "Orang tua mendorong saya untuk membicarakan masalah yang saya alami") 
        radio_question(driver, "orang tua memahami perasaan saya")
        radio_question(driver, "Orang tua mengerti kebutuhan saya")
        radio_question(driver, "Orang tua memberikan kenyamanan ketika saya sedang kesal")
        radio_question(driver, "Orang tua memberikan pujian apabila saya berbuat baik")
        radio_question(driver, "Orang tua meluangkan waktu khusus untuk bersama saya")
        radio_question(driver, "Orang tua memberikan alasan kepada saya mengapa peraturan harus dipatuhi")
        radio_question(driver, "orang tua membantu saya agar dapat memahami dampak dari suatu perilaku dengan cara mendorong saya agar dapat memaparkan apa saja akibat-akibat dari suatu perbuatan saya")
        radio_question(driver, "Orang tua menjelaskan kepada saya tentang akibat-akibat dari masalah yang saya lakukan")
        radio_question(driver, "orang tua saya menekankan alasan mengapa suatu peraturan itu dibuat.")
        radio_question(driver, "Orang tua menghargai pendapat saya")
        radio_question(driver, "Orang tua mendorong saya untuk mengutarakan pendapat saya")
        radio_question(driver, "Orang tua mendorong saya untuk bebas berekspresi meskipun ada perbedaan paham dengan orang tua saya")
        radio_question(driver, "Orang tua memberikan saya kesempatan untuk memberi masukan terhadap peraturan keluarga")
        radio_question(driver, "Orang tua memperhatikan keinginan saya sebelum meminta saya melakukan sesuatu.")
        radio_question(driver, "Orang tua mempertimbangkan minat saya dalam membuat rencana-rencana keluarga.")
        radio_question(driver, "Orang tua menyatakan hukuman kepada saya akan tetapi tidak benar-benar dilakukannnya.")
        radio_question(driver, "Orang tua lebih sering menyampaikan ancaman kepada saya untuk memberikan hukuman namun tidak melaksanakan ancaman tersebut")
        radio_question(driver, "Orang tua tidak melakukan apapun ketika saya menyebabkan masalah tentang sesuatu")
        radio_question(driver, "Orang tua tidak mendisiplinkan saya")
        radio_question(driver, "Orang tua mengikuti atau mengabulkan apapun yang saya inginkan") 
        radio_question(driver, "Orang tua memberikan hadiah ketika saya mengikuti perintahnya")
        radio_question(driver, "Orang tua tidak pernah menegur apabila saya melakukan kesalahan")
        radio_question(driver, "Orang tua membela saya walaupun saya berbuat salah")
        radio_question(driver, "Orang tua tidak pernah menegur apabila saya berlaku tidak sopan kepada orang lain")
        next_page_button(driver)
        
        radio_question(driver, "Saya merasa... mampu memilih satu jurusan diantara berbagai jurusan potensial yang saya pertimbangkan")
        radio_question(driver, "Saya ....... mampu memilih jurusan atau karir yang sesuai dengan minat saya")
        radio_question(driver, "Saya ....... dapat mengukur kemampuan saya secara tepat.")
        radio_question(driver, "Saya… mampu memperoleh informasi dari internet mengenai pekerjaan yang saya minati.")
        radio_question(driver, "Saya ....... mampu menemukan tren untuk suatu pekerjaan pada lebih dari 10 tahun mendatang")
        radio_question(driver, "Saya ....... mampu memiliki pengetahuan mengenai penghasilan rata-rata per tahun yang akan didapat individu dari suatu pekerjaan")
        radio_question(driver, "Saya ....... mampu berdiskusi dengan orang yang sudah bekerja di bidang yang saya minati")
        radio_question(driver, "Saya .......  mampu mengenali karyawan, perusahaan, institusi yang relevan dengan kemungkinan karir saya.")
        radio_question(driver, "Saya ....... mampu mencari informasi mengenai sekolah profesi atau pasca-sarjana")
        radio_question(driver, "Saya ....... mampu memperoleh dukungan (emosional, dana/finansial, informasi, dll.) terkait dengan pilihan jurusan atau karir yang saya minati")
        radio_question(driver, "Saya ....... mampu membuat rencana mengenai tujuan pekerjaan saya untuk lima tahun mendatang")
        radio_question(driver, "Saya ....... mampu memilih satu pekerjaan dari berbagai pekerjaan potensial bagi masa depan saya")
        radio_question(driver, "Saya ....... dapat bekerja dalam bidang atau tujuan karir saya")
        radio_question(driver, "Saya...... dapat mencapai sukses bahkan ketika saya merasa frustrasi")
        radio_question(driver, "Saya ....... dapat menentukan apa pekerjaan ideal saya")
        radio_question(driver, "Saya ....... dapat memilih karir yang akan sesuai/cocok dengan gaya hidup saya")
        radio_question(driver, "Saya ....... mampu dalam menentukan hal apa yang saya nilai paling penting dalam sebuah pekerjaan")
        radio_question(driver, "Saya ....... mampu menentukan langkah-langkah yang perlu diambil untuk dapat menyelesaikan jurusan yang saya pilih dengan sukses")
        radio_question(driver, "Saya ....... mampu menyiapkan CV yang baik/bagus")
        radio_question(driver, "Saya ....... mampu menemukan alternatif pilihan jurusan lain bila nantinya saya mengalami hambatan pada jurusan yang saya pilih")
        radio_question(driver, "Saya ....... dapat lulus proses seleksi wawancara pada pekerjaan yang saya minati")
        radio_question(driver, "Saya ....... mampu memperoleh dukungan dari keluarga terkait jurusan atau karir yang saya minati")
        radio_question(driver, "Kemahiran saya dalam bidang tertentu di kampus membuat saya semakin ....... mampu memilih karir di masa depan")
        radio_question(driver, "Saya ....... bahwa prestasi non-akademik yang saya capai sudah cukup memenuhi persyaratan dari jurusan atau karir yang saya minati")
        radio_question(driver, "Saya ....... dapat menemukan solusi terhadap masalah akademik dan non-akademik pada jurusan yang akan saya pilih")
        radio_question(driver, "Saya ....... dapat membuat keputusan terhadap karir tanpa rasa khawatir (apakah benar atau salah), mengenai karir yang akan saya tempuh")
        radio_question(driver, "Saya ....... mampu menemukan alternatif pilihan karir lain bila nantinya saya mengalami hambatan pada karir yang saya pilih")
        radio_question(driver, "Saya ....... mampu mencari beberapa alternatif jurusan lain jika saya tidak diterima di jurusan yang saya minati")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()