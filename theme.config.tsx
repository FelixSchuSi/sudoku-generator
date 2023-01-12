import React from 'react'
import { DocsThemeConfig } from 'nextra-theme-docs'
import { useRouter } from 'next/router';

const config: DocsThemeConfig = {
  logo: <span>Sudoku Generator</span>,
  project: {
    link: 'https://github.com/FelixSchuSi/sudoku-generator',
  },
  docsRepositoryBase: 'https://github.com/FelixSchuSi/sudoku-generator/tree/main/',
  footer: {
    text: 'Nextra Docs Template',
  },
  editLink: {
    text: () => {
      const { locale } = useRouter();
      switch (locale) {
        case "de":
        default:
          return <p>Bearbeite diese Seite auf GitHub →</p>
      }
    },
  },
  feedback: {
    content: () => {
      const { locale } = useRouter();
      switch (locale) {
        case "de":
        default:
          return <p>Frage? Gib uns Feedback →</p>
      }
    },
  },
  toc: {
    title: () => {
      const { locale } = useRouter();
      switch (locale) {
        case "de":
        default:
          return <>Auf dieser Seite</>
      }
    },
  },
  search: {
    placeholder: () => {
      const { locale } = useRouter();
      switch (locale) {
        case "de":
        default:
          return "Suchen..."
      }
    },
  },
  gitTimestamp: ({ timestamp }) => {
    const { locale } = useRouter();
    console.log(timestamp);
    switch (locale) {
      case "de":
      default:
        return <>Zuletzt aktualisiert am {new Intl.DateTimeFormat('de', { dateStyle: 'long' }).format(timestamp)}</>
    }
  },
  i18n: [
    { locale: 'de', text: 'Deutsch' }
  ],

}

export default config
