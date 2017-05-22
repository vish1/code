'''Whatsapp Question:
Find English words by adding the same letter as the first and last character to the following chunks:
_ivi_ 	_rus_
_ido_	_rom_
_useu_	_athtu_
_ras_	_ypis_
_eapo_	_ardia_
_ero_	_ende_
_hroa_	_regan_
_umm_	_oile_
_omi_	_abe_
_lini_	_wis_

'''
import string, enchant, pprint
qs= [
	'ivi', 'rus', 'ido', 'rom', 'useu', 'athtu', 'ras', 'ypis', 'eapo', 'ardia', 
	'ero', 'ende', 'hroa', 'regan', 'umm', 'oile', 'omi', 'abe', 'lini', 'wis'
	]
pprint.pprint([(q, l+q+l) for q in qs for l in list(string.ascii_lowercase)  if enchant.Dict("en_US").check(l+q+l)])

'''Output:
[('ivi', 'civic'),
 ('rus', 'trust'),
 ('ido', 'widow'),
 ('rom', 'aroma'),
 ('useu', 'museum'),
 ('athtu', 'bathtub'),
 ('ras', 'erase'),
 ('ypis', 'typist'),
 ('eapo', 'teapot'),
 ('ardia', 'cardiac'),
 ('ero', 'xerox'),
 ('ende', 'render'),
 ('hroa', 'throat'),
 ('regan', 'oregano'),
 ('umm', 'yummy'),
 ('oile', 'toilet'),
 ('omi', 'comic'),
 ('abe', 'label'),
 ('lini', 'clinic'),
 ('wis', 'swiss'),
 ('wis', 'twist')]
 '''
