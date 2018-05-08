from ba_ma import BaseConverter

base58 = BaseConverter(
  'ABCDEFGHJKLMNPQRSTUVWXYZ123456789abcdefghijkmnopqrstuvwxyz'
)

class CollapseAddressSpace():
	space_ca = {}
	hop_char = 5

	def compute_address(self, addr):
		for i in range(CollapseAddressSpace.hop_char, len(addr), CollapseAddressSpace.hop_char):
			indx = addr[i-CollapseAddressSpace.hop_char:i]
			print i, indx
			CollapseAddressSpace.space_ca[indx] = CollapseAddressSpace.space_ca.get(indx, 0) + 1

	def collapse(self):
		print CollapseAddressSpace.space_ca.keys()

	def calc_network_index(self, index_st):
		r = base58.to_decimal(index_st) 
		print index_st, r
		return r

cass = CollapseAddressSpace()
cass.compute_address ("XtuVUju4Baaj7YXShQu4QbLLR7X2aw9Gc8")
cass.compute_address ("XbmPwcZCdaRMa4m4JedspBPkUqY1FKRhsX")
cass.compute_address ("XgfLsphG9KDGmyBEwHmBjMRYa8Hr7Yode5")
cass.compute_address ("XxYTj1hgGMx6X6PgFmTsq4zcMkhrSMczTJ")
cass.compute_address ("Xo9UzA2B7yyEhsrQZyFPGCTuFbNGKgHkPU")
cass.collapse()

print "storage vector c"
print cass.calc_network_index("XtuVU") - cass.calc_network_index("XAAAA")

print "start vector c"
print cass.calc_network_index("XAAAA")

print "final possible vector"
print cass.calc_network_index("Xzzzz")