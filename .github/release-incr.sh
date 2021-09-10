cur_version=`cat pylark/__init__.py | grep version__ | cut -d '=' -f 2-2 | xargs`
echo "cur_version: $cur_version"

cur_version_last=`echo $cur_version | cut -d '.' -f 3-3`
echo "cur_version_last: $cur_version_last"

new_version_last=$((cur_version_last+1))
new_version="0.0.$new_version_last"
echo "new_version: $new_version"

gsed -i 's/__version__ = "'$cur_version'"/__version__ = "'$new_version'"/g' pylark/__init__.py
gsed -i 's/version = "'$cur_version'"/version = "'$new_version'"/g' pyproject.toml

git commit -a -m "release: v$new_version"
git tag "v$new_version"

poetry publish
