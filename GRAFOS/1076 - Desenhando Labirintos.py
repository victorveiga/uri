def GetGrafo():
	vInicial = int(input());
	iVertices, iArestas = input().split(' ');
	xArestas = [];
	for i in range(int(iArestas)):
		iA, iB = input().split(' ');
		if (int(iA) > int(iB)):
			iA, iB = iB, iA;

		if not ((int(iA), int(iB)) in xArestas):
			xArestas.append((int(iA), int(iB)));
	return xArestas;

iQtdeGrafos = int(input());
xListaGrafos = [];
for n in range(iQtdeGrafos):
	xListaGrafos.append(GetGrafo());

for n in xListaGrafos:
	print('{}'.format((len(n) * 2)));