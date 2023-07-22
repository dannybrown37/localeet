import random

import requests
from bs4 import BeautifulSoup

from pprint import pprint

ROOT = 'https://leetcode.com'
API_URL = f'{ROOT}/api/problems/all/'
GQL_URL = f'{ROOT}/graphql'


def get_random_leetcode_question() -> dict:
    response = requests.get(API_URL).json()['stat_status_pairs']
    return random.choice(response)['stat']


def get_question_text_for_question(question_metadata: dict):
    payload = {
        "operationName": "questionData", 
        "variables": {
            "titleSlug": question_metadata['question__title_slug']
        },
        "query": """query questionData($titleSlug: String!) {
                        question(titleSlug: $titleSlug) {
                            questionId
                            questionFrontendId
                            boundTopicId
                            title
                            titleSlug
                            content
                            translatedTitle
                            translatedContent
                            isPaidOnly
                            difficulty
                            likes
                            dislikes
                            isLiked
                            similarQuestions
                            contributors {
                                username
                                profileUrl
                                avatarUrl
                                __typename
                            }
                            langToValidPlayground
                            topicTags {
                                name
                                slug
                                translatedName
                                __typename
                            }
                            companyTagStats
                            codeSnippets {
                                lang
                                langSlug
                                code
                                __typename
                            }
                            stats
                            hints
                            solution {
                                id
                                canSeeDetail
                                __typename
                            }
                            status
                            sampleTestCase
                            metaData
                            judgerAvailable
                            judgeType
                            mysqlSchemas
                            enableRunCode
                            enableTestMode
                            envInfo
                            libraryUrl
                            __typename
                        }
                    }
                """
    }

    response = requests.post(GQL_URL, json=payload).json()
    soup = BeautifulSoup(response['data']['question']['content'], 'lxml')
    title = response['data']['question']['title']
    question =  soup.get_text().replace('\n',' ')
    print(title, '\n', question)


def run_series():
    question_metadata = get_random_leetcode_question()
    result = get_question_text_for_question(question_metadata)
   