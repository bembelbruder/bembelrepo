#!/bin/sh

rm -r /home/sascha/addons/script.module.bembelresolver/*
rm /home/sascha/addons/script.module.bembelresolver.zip

cp -r ../script.module.bembelresolver /home/sascha/addons/
cd /home/sascha/addons/
python addons_xml_generator.py
zip -r script.module.bembelresolver.zip script.module.bembelresolver/

scp addons.xml* pi@rasp-wohn:/var/www/
scp script.module.bembelresolver.zip pi@rasp-wohn:/var/www/script.module.bembelresolver/

