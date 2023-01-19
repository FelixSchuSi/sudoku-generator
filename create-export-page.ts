import { promises as fs } from 'fs'
const path = require('path');

const pagesDir = path.join(process.cwd(), 'pages')
const exportFile = path.join(process.cwd(), 'pages','export.mdx')

const data = JSON.parse(`
[{"kind":"MdxPage","name":"index","route":"/","meta":{"title":"Sudoku Generator","type":"page","display":"hidden"}},{"kind":"MdxPage","name":"export","route":"/export","meta":{"title":"Export","display":"hidden"}},{"kind":"Folder","name":"basiswissen","route":"/basiswissen","children":[{"kind":"MdxPage","name":"literaturempfehlungen","route":"/basiswissen/literaturempfehlungen","meta":{"title":"Literaturempfehlungen"}},{"kind":"MdxPage","name":"grover","route":"/basiswissen/grover","meta":{"title":"Grover Algorithmus"}}],"meta":{"title":"Basiswissen","type":"page"}},{"kind":"Folder","name":"quantenalgorithmus","route":"/quantenalgorithmus","children":[{"kind":"Folder","name":"uebersicht","route":"/quantenalgorithmus/uebersicht","children":[{"kind":"MdxPage","name":"bestandteile","route":"/quantenalgorithmus/uebersicht/bestandteile","meta":{"title":"Bestandteile"}},{"kind":"MdxPage","name":"demo-anwendung","route":"/quantenalgorithmus/uebersicht/demo-anwendung","meta":{"title":"Demo Anwendung"}}],"meta":{"title":"Übersicht"}},{"kind":"Folder","name":"algorithmus-im-detail","route":"/quantenalgorithmus/algorithmus-im-detail","children":[{"kind":"MdxPage","name":"candidates","route":"/quantenalgorithmus/algorithmus-im-detail/candidates","meta":{"title":"Candidates"}},{"kind":"MdxPage","name":"edges","route":"/quantenalgorithmus/algorithmus-im-detail/edges","meta":{"title":"Edges"}},{"kind":"MdxPage","name":"cubit-registry","route":"/quantenalgorithmus/algorithmus-im-detail/cubit-registry","meta":{"title":"Cubit Registry"}},{"kind":"MdxPage","name":"init-blanks","route":"/quantenalgorithmus/algorithmus-im-detail/init-blanks","meta":{"title":"Init Blanks"}},{"kind":"MdxPage","name":"oracle","route":"/quantenalgorithmus/algorithmus-im-detail/oracle","meta":{"title":"Oracle"}},{"kind":"MdxPage","name":"diffusor","route":"/quantenalgorithmus/algorithmus-im-detail/diffusor","meta":{"title":"Diffusor"}},{"kind":"MdxPage","name":"messen-und-ausfuehren","route":"/quantenalgorithmus/algorithmus-im-detail/messen-und-ausfuehren","meta":{"title":"Messen und Ausführen"}},{"kind":"MdxPage","name":"ergebnis-parsen","route":"/quantenalgorithmus/algorithmus-im-detail/ergebnis-parsen","meta":{"title":"Ergebnis parsen"}},{"kind":"MdxPage","name":"ergebnis-ueberpruefen-und-messen","route":"/quantenalgorithmus/algorithmus-im-detail/ergebnis-ueberpruefen-und-messen","meta":{"title":"Ergebnis überprüfen und messen"}}],"meta":{"title":"Algorithmus im Detail"}},{"kind":"MdxPage","name":"entwicklung","route":"/quantenalgorithmus/entwicklung","meta":{"title":"Entwicklung"}},{"kind":"MdxPage","name":"zusammenfassung","route":"/quantenalgorithmus/zusammenfassung","meta":{"title":"Zusammenfassung"}}],"meta":{"title":"Quantenalgorithmus","type":"page"}},{"kind":"Folder","name":"videos","route":"/videos","children":[{"kind":"MdxPage","name":"videos","route":"/videos/videos","meta":{"title":"Videos"}}],"meta":{"title":"Videos","type":"page"}},{"kind":"Folder","name":"benchmarks","route":"/benchmarks","children":[{"kind":"MdxPage","name":"benchmarks","route":"/benchmarks/benchmarks","meta":{"title":"Benchmarks"}}],"meta":{"title":"Benchmarks","type":"page"}}]
`)

function parseData(data: any[]) {
    const result = [];
    for (let item of data) {
        if (item.kind === 'MdxPage') {
            result.push({path: item.name + '.mdx', title: item.meta.title ?? item.name});
        } else if (item.kind === 'Folder') {
            result.push({path: item.name, title: item.meta.title ?? item.name});
            const children = parseData(item.children);
            result.push(...children.map(c => {return {path: item.name + '/' + c.path, title: c.title}}));
        }
    }
    return result;
}

async function main(filesAndDirs: {path: string, title: string}[]) {
  const content = await Promise.all(filesAndDirs.map(async f => {
    if (f.path.includes("export")) return "";
    const level = f.path.split('/').length;
    if (!f.path.includes('.')) return `${'#'.repeat(level)} ${f.title}`;
    const fileContent = await fs.readFile(path.join(pagesDir,f.path), 'utf8');
    const result = [];
    for (let line of fileContent.split('\n')) {
        if (line.startsWith('#')) {
            result.push('#'.repeat(level -1) + line);
        } else {
            result.push(line);
        }
    }
    return result.join("\n");
  }));
  await fs.writeFile(exportFile, content.join('\n\n'))
}

main(parseData(data));