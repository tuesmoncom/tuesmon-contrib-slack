#!/bin/sh

make || exit 1
rm -rf /tmp/tuesmon-contrib-slack-doc-dist || exit 1
cp -r dist /tmp/tuesmon-contrib-slack-doc-dist || exit 1
git checkout gh-pages || exit 1
rm -rf dist || exit 1
mv /tmp/tuesmon-contrib-slack-doc-dist ../dist || exit 1
git add --all ../dist || exit 1
git commit -a -m "Update doc" || exit 1
