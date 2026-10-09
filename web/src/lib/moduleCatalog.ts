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
    tagline: "Complexity, patterns, interview readiness",
    hue: 57,
  },
  {
    id: "frontend-basics",
    label: "Frontend foundations",
    tagline: "Readable interfaces with resilient UX",
    hue: 105,
  },
  {
    id: "javascript-typescript",
    label: "JavaScript & TypeScript",
    tagline: "Runtime safety with practical TypeScript patterns",
    hue: 153,
  },
  {
    id: "backend",
    label: "Backend",
    tagline: "APIs, auth, reliability, and service boundaries",
    hue: 172,
  },
  {
    id: "system-design",
    label: "System design",
    tagline: "Design choices for growth, latency, and reliability",
    hue: 201,
  },
  {
    id: "devops",
    label: "DevOps",
    tagline: "Build, release, observe, and recover confidently",
    hue: 268,
  },
  {
    id: "dbms",
    label: "Databases",
    tagline: "Queries, indexes, transactions, data correctness",
    hue: 220,
  },
];

export const MODULE_IDS = MODULE_CATALOG.map((m) => m.id);

export function moduleMeta(id: string): ModuleMeta | undefined {
  return MODULE_CATALOG.find((m) => m.id === id);
}
