#该网站通过爬取豆瓣上的书籍，并根据其他信息对书籍的评分做了新的计算。

*   书籍之间的关系按照标签组织在一起，而用户可以通过收藏标签来获取高排名的书籍<br>

    书籍的涉及如下因素：1：给出评分的用户数量， 2：想读，在读，已读的用户数量，3：书籍涉及到的豆列数量，4：给出评价的用户数量<br>

    每个因素都采用如下公式计算：f(x) = x / (m + x). 其中m是固定参数<br>

*   涉及到的技术<br>
    爬虫:Beautifulsoup4, request<br>

    数据库:mongodb,mongoengine<br>

    缓存:redis,redis-py<br>

    框架:Flask<br>

    监控:supervisor<br>

    前端:bootstrap<br>
    网址:[book_rank](http://bookrank.cn)
*   关于作者<br>
    [林通](https://www.github.com/hellolintong)<br>

    [李松峰](https://github.com/lisongfeng9213)<br>
