import React from 'react'
import { DocsThemeConfig, useConfig } from 'nextra-theme-docs'
import { useTheme } from 'next-themes'
import { useRouter } from 'next/router';
import Image from 'next/image';
import Logo from './logo';



const config: DocsThemeConfig = {
  logo: Logo,
  project: {
    link: 'https://github.com/FelixSchuSi/sudoku-generator',
  },
  docsRepositoryBase: 'https://github.com/FelixSchuSi/sudoku-generator/tree/main/',
  footer: {
    text: () => {
      const { locale } = useRouter();
      switch (locale) {
        case "de":
        default:
          return <p>Von Tizian Lengemann, Jannik Bergjan und <a className="nx-font-medium nx-text-gray-500 hover:nx-text-gray-900 dark:nx-text-gray-400 dark:hover:nx-text-gray-100 contrast-more:nx-text-gray-800 contrast-more:dark:nx-text-gray-50" href="https://github.com/FelixSchuSi">Felix Schulze Sindern</a></p>
      }
    }
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
    switch (locale) {
      case "de":
      default:
        return <>Zuletzt aktualisiert am {new Intl.DateTimeFormat('de', { dateStyle: 'long' }).format(timestamp)}</>
    }
  },
  head: () => {
    return <>
      <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
      <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
      <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
      <link rel="manifest" href="/site.webmanifest" />
      <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#5bbad5" />
      <meta name="msapplication-TileColor" content="#da532c" />
      <meta name="theme-color" content="#ffffff" />
    </>
  },
  i18n: [
    { locale: 'de', text: 'Deutsch' }
  ],

}

export default config
