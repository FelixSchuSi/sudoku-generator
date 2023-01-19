import { promises as fs } from 'fs'
const path = require('path');

const pagesDir = path.join(process.cwd(), 'pages')
const exportFile = path.join(process.cwd(), 'pages','export.mdx')

async function findAllMdxFiles(dir): Promise<string[]> {
    const filesAndDirs = await fs.readdir(path.join(pagesDir,dir));
    const result =  await Promise.all(filesAndDirs.flatMap(async (fileOrDir) => {
        if (fileOrDir.includes('.mdx')) return [path.join(dir, fileOrDir)];
        if (!fileOrDir.includes('.')) {
            return await findAllMdxFiles(path.join(dir, fileOrDir));
        }
        return [];
    }));
    return result.flat();
}

async function main() {
  const files = await findAllMdxFiles("");
  console.log(files)
  const content = await Promise.all(files.map(async f => {
    if (f.includes("export")) return "";
    const fileContent = await fs.readFile(path.join(pagesDir,f), 'utf8');
    const level = f.split('/').length -1;
    console.log(level, f);
    const result = [];
    for (let line of fileContent.split('\n')) {
        if (line.startsWith('#')) {
            result.push('#'.repeat(level) + line);
        } else {
            result.push(line);
        }
    }
    return fileContent;
  }));
  await fs.writeFile(exportFile, content.join('\n\n'))
}

main();