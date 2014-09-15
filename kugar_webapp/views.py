# coding=utf-8
from django.shortcuts import render
import feedparser
from models import Feedkik
# Create your views here.


def main(request):
    return render(request, 'main.html')

def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')

def search(keywords):
    search_results = []

    url_1 = 'https://kickass.to/usearch/'
    url_2 = '/?rss=1'
    feed = feedparser.parse(url_1+keywords.lower()+url_2)

    for entry in feed['entries']:
        title = entry['title']
        published_parsed = entry['published']
        links = entry['links'][0]['href']
        link = entry['links'][1]['href']
        torrent_seeds = entry['torrent_seeds']
        torrent_peers = entry['torrent_peers']
        description = "No description"
        magnet = entry['torrent_magneturi']
        feed_new = Feedkik()
        feed_new.title = title
        feed_new.published_parsed = published_parsed
        feed_new.links = links
        feed_new.link = link
        feed_new.torrent_seeds = torrent_seeds
        feed_new.torrent_peers = torrent_peers
        feed_new.description = description
        feed_new.magnet = magnet

        search_results.append(feed_new)

    return search_results


def results(request):
    if 'srch-term' in request.GET and request.GET['srch-term']:
        srch_term = request.GET['srch-term']
        feeds = search(srch_term)
        return render(request, 'results.html', {'feeds': feeds, 'query': srch_term})
