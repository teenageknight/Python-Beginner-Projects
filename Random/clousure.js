function html_tag(tag){
  function wrap_text(msg) {
    console.log('<' + tag +'>' + msg + '</' + tag + '>')
  }
  return wrap_text
}

var print_h1 = html_tag('h1')

print_h1("Test Headline")
print_h1("Another Headline")
