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
    hue: 134,
  },
  {
    id: "frontend-basics",
    label: "Frontend foundations",
    tagline: "Readable interfaces with resilient UX",
    hue: 182,
  },
  {
    id: "javascript-typescript",
    label: "JavaScript & TypeScript",
    tagline: "Runtime safety with practical TypeScript patterns",
    hue: 230,
  },
  {
    id: "backend",
    label: "Backend",
    tagline: "Production-grade endpoints and failure handling",
    hue: 249,
  },
  {
    id: "system-design",
    label: "System design",
    tagline: "Scale, tradeoffs, and architecture judgement",
    hue: 278,
  },
  {
    id: "devops",
    label: "DevOps",
    tagline: "Build, release, observe, and recover confidently",
    hue: 25,
  },
  {
    id: "dbms",
    label: "Databases",
    tagline: "Queries, indexes, transactions, data correctness",
    hue: 297,
  },
];

export const MODULE_IDS = MODULE_CATALOG.map((m) => m.id);

export function moduleMeta(id: string): ModuleMeta | undefined {
  return MODULE_CATALOG.find((m) => m.id === id);
}
