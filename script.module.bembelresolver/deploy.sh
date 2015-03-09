name="script.module.bembelresolver"
version=`grep -o -a -m 1 -h -r '[0-9]\.[0-9]\.[0-9]' addon.xml`

cp -r ../$name ../datadir/$name

cd ../datadir/$name
zip -r $name-${version}.zip $name/
rm -rf $name

cd ..
python addons_xml_generator.py
