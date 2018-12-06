import os, git, json

note_md_prefix = (
    "---\nlayout: page\npermalink: /notes/index.html\ntitle: Notes\nnotes:\n"
)
note_md_suffix = "---\n# Notes\n\n{% for note in page.notes %}\n{% unless note.hidden %}\n  - {% if note.url %} [{{note.title}}]({{note.url}}).\n    {% else %} {{note.title}}.\n    {% endif %}<br>\n    {{note.author}}.<br>\n    {{note.date}}.<br>\n{% endunless %}\n{% endfor %}\n"

def json2md(json_file, md_file, check_list):
    #read notes.json
    with open(json_file) as f:
        data = json.loads(f.read())
    with open(md_file, "w") as f:
        f.write(note_md_prefix)
        for item in data:
            item_str = '- author: "%s"\n  title: "%s"\n  date: "%s"\n  url: %s\n  hidden: %s \n\n' % (
                item['author'], item['title'], item['date'], item['url'], 'false' if item['hidden'] else 'true'
            )
            if item['url'] not in check_list:
                print("%s does not exist in ../notes/" % item['url'])
            else:
                print("%s done." % item['url'])
            f.write(item_str)
        f.write(note_md_suffix)

def push():
    repo = git.Repo()
    g = repo.git
    g.add('.')
    g.commit('-m "..."')
    rmt = repo.remote()
    rmt.pull()
    rmt.push()

if __name__ == "__main__":
    print('Hello')
    check_list = os.listdir(os.getcwd()+"/notes")
    print('convert json to markdown...')
    json2md("notes.json", "notes.md", check_list)
    print('push...')
    push()

