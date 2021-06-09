from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scraputils import get_news

Base = declarative_base()
engine = create_engine("sqlite:///news.db")
session = sessionmaker(bind=engine)


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    url = Column(String)
    comments = Column(Integer)
    points = Column(Integer)
    label = Column(String)

Base.metadata.create_all(bind=engine)



if __name__ == "__main__":
    news_list = get_news("https://news.ycombinator.com/newest", n_pages=20)
    length = len(news_list)
    s = session()
    for i in range(length):
        news = News(
            title=news_list[i]["title"],
            author=news_list[i]["author"],
            url=news_list[i]["link"],
            comments=news_list[i]["comments"],
            points=news_list[i]["points"],
        )
        s.add(news)
        s.commit()



