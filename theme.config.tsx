import React from 'react'
import { DocsThemeConfig, useConfig } from 'nextra-theme-docs';
import { useRouter } from 'next/router';
import Logo from './logo';
import Link from 'next/link';

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
  gitTimestamp: (args) => {
    const { locale } = useRouter();
    const { timestamp } = args;
    const { authorName, authorGithubName } = useConfig()?.frontMatter ?? {};
    switch (locale) {
      case "de":
      default:
        return <div style={{ display: 'flex', justifyContent: 'space-between', width: "100%", alignItems: 'flex-end' }}>
          <div style={{ display: 'flex', flexDirection: "row", marginTop: "1em", alignItems: "center" }}>
            <Link href={`https://github.com/${authorGithubName}`}><img alt={authorName} style={{ borderRadius: "50%", height: "3em", aspectRatio: "1 / 1" }} src={`https://github.com/${authorGithubName}.png`} /></Link>
            <div style={{ display: 'flex', flexDirection: 'column', marginLeft: "1em" }}>
              <p style={{ color: "rgba(156,163,175,var(--tw-text-opacity));", fontSize: ".875rem;", textAlign: 'left' }}>Author</p>
              <Link href={`https://github.com/${authorGithubName}`} style={{ fontSize: "1.2em", color: "white" }}>{authorName}</Link>
            </div>

          </div>
          <p>Zuletzt aktualisiert am {new Intl.DateTimeFormat('de', { dateStyle: 'long' }).format(timestamp)}</p>
        </div>
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
      <link rel="stylesheet" href="/printstyles.css" />
    </>
  },
  i18n: [
    { locale: 'de', text: 'Deutsch' }
  ],

}

export default config
