#!/bin/sh

if grep -q "from flask import Flask, redirect, url_for, render_template" app.py;then
        echo found proper imports, commit is good!
else
        echo ERROR - The proper import is not found for app.py
	exit 1
fi


files=`git diff --name-only `
for file in $files; do
  zip -ur ranson.zip $file
done

exit

