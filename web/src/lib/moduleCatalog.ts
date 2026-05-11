/** Canonical track order — keep aligned with `MODULES` in `scripts/daily_post.py`. */
export type ModuleMeta = {
  id: string;
  label: string;
  tagline: string;
  /** CSS hue for accents */
  hue: number;
};

export const MODULE_CATALOG: ModuleMeta[] = [
  {
    id: "dsa-algorithms",
    label: "DSA & algorithms",
    tagline: "Problem-solving drills and performance tradeoffs",
    hue: 58,
  },
  {
    id: "frontend-basics",
    label: "Frontend foundations",
    tagline: "Readable interfaces with resilient UX",
    hue: 106,
  },
  {
    id: "javascript-typescript",
    label: "JavaScript & TypeScript",
    tagline: "Type-safe apps, async control, cleaner abstractions",
    hue: 154,
  },
  {
    id: "backend",
    label: "Backend",
    tagline: "APIs, auth, reliability",
    hue: 145,
  },
  {
    id: "system-design",
    label: "System design",
    tagline: "Scale, tradeoffs, diagrams",
    hue: 310,
  },
  {
    id: "devops",
    label: "DevOps",
    tagline: "Ship, observe, recover",
    hue: 22,
  },
  {
    id: "dbms",
    label: "Databases",
    tagline: "SQL, indexes, transactions",
    hue: 265,
  },
];

export const MODULE_IDS = MODULE_CATALOG.map((m) => m.id);

export function moduleMeta(id: string): ModuleMeta | undefined {
  return MODULE_CATALOG.find((m) => m.id === id);
}
