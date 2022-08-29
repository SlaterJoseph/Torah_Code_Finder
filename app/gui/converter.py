def create_converter(variant: str) -> dict:
    if variant == 'letter':
        version = 'just_char'
    else:
        version = 'words'

    converter = dict()
    converter['חומש'] = 'app/texts/' + version + '/chumash.txt'
    converter['בראשית'] = 'app/texts/' + version + '/genesis.txt'
    converter['שמות'] = 'app/texts/' + version + '/exodus.txt'
    converter['ויקרא'] = 'app/texts/' + version + '/leviticus.txt'
    converter['במדבר'] = 'app/texts/' + version + '/numbers.txt'
    converter['דברים'] = 'app/texts/' + version + '/deuteronomy.txt'
    converter['אסתר'] = 'app/texts/' + version + '/esther.txt'
    converter['שיר השירים'] = 'app/texts/' + version + '/shir.txt'
    return converter
