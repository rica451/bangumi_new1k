import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def get_all_score(subject_id):
    url = f"https://api.jirehlov.com/vib/{subject_id}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        status_forcelist=[403, 429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    response = session.get(url, headers=headers)
    response.raise_for_status()  # 检查响应状态码
    data = response.json()
    all_score = data.get("ALL_score")
    return all_score

if __name__ == "__main__":
    with open('url_list.txt', 'r') as file:
        subject_ids = [line.strip().split('/')[-1] for line in file.readlines()]

    with open('all_scores.txt', 'w') as output_file:
        for subject_id in subject_ids:
            try:
                all_score = get_all_score(subject_id)
                output_file.write(f"Subject ID: {subject_id}, ALL_score: {all_score}\n")
            except requests.exceptions.HTTPError as e:
                output_file.write(f"Failed to retrieve ALL_score for Subject ID: {subject_id}, Error: {e}\n")