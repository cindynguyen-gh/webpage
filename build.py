top_template = open('./templates/top.html').read()
bottom_template = open('./templates/bottom.html').read()

index = open('./content/index.html').read()
index_html = top_template + index + bottom_template
open('./docs/index.html', 'w+').write(index_html)

portfolio = open('./content/portfolio.html').read()
portfolio_html = top_template + portfolio + bottom_template
open('./docs/portfolio.html', 'w+').write(portfolio_html)

about = open('./content/about.html').read()
about_html = top_template + about + bottom_template
open('./docs/about.html', 'w+').write(about_html)

contacts = open('./content/contacts.html').read()
contacts_html = top_template + contacts + bottom_template
open('./docs/contacts.html', 'w+').write(contacts_html)




