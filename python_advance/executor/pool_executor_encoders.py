import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from sentence_transformers import SentenceTransformer


def enc_s1(text):
    sbert1 = SentenceTransformer('distiluse-base-multilingual-cased-v1')
    return sbert1.encode(text)


def enc_s2(text):
    sbert2 = SentenceTransformer('paraphrase-xlm-r-multilingual-v1')
    return sbert2.encode(text)


def enc_s3(text):
    sbert3 = SentenceTransformer('LaBSE')
    return sbert3.encode(text)


def get_sent_emb(text):
    return [enc_s1(text), enc_s2(text), enc_s3(text)]


if __name__ == '__main__':
    sec = 5
    num = 200000000

    train_text = [
        'These models find semantically similar sentences within one language or across languages.',
        'Bitext mining describes the process of finding translated sentence pairs in two languages.',
        'If this is your use-case, the following model gives the best performance.'
    ]
    
    start = time.time()
    with ThreadPoolExecutor(max_workers=8) as executor:
        embs = [executor.submit(enc_s1, train_text), executor.submit(enc_s2, train_text, ),
                executor.submit(enc_s3, train_text, )]
        embs_final = [e.result() for e in embs]
    print(f'The time taken by thread pool={time.time() - start}')

    start = time.time()
    with ProcessPoolExecutor(max_workers=8) as executor:
        embs = [executor.submit(enc_s1, train_text), executor.submit(enc_s2, train_text, ),
                executor.submit(enc_s3, train_text, )]
        embs_final = [e.result() for e in embs]
    print(f'The time taken by thread pool={time.time() - start}')
    print(f'The time taken by process pool={time.time() - start}')
