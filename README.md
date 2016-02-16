blog de JP Roussaffa
====
http://jproussaffa.pythonanywhere.com


hebergeur pythonanywhere : Pack gratuit (500 Mo) 
Python : 2.7 
Pelican : 3.5

Automatisation des déploiements desktop -> git -> pythonanywhere


````sh
cd projects/
git clone git://github.com/yougis/blog-jp.git
git clone git://github.com/yougis/pure-single-jp.git
git clone git://github.com/yougis/flickr.git

git clone git://github.com/getpelican/pelican-plugins.git
cd pelican-plugins
git clone git://github.com/La0/pelican-flickr.git


virtualenv envpelican
source /projects/bin/activate 


cd pelican-plugin/pelican-flickr
sudo python setup.py install
pip install pelican

pip install markdown
pip install pelican-flickr

pelican-themes --install pure-single-jp
````sh

need plugins :
- pelican-flickr
- liquid_tags
- sitemap

//pelcan-themes install pure-sigle-jp