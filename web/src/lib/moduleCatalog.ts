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
    hue: 225,
  },
  {
    id: "frontend-basics",
    label: "Frontend foundations",
    tagline: "UI structure, accessibility, and rendering speed",
    hue: 273,
  },
  {
    id: "javascript-typescript",
    label: "JavaScript & TypeScript",
    tagline: "Type-safe apps, async control, cleaner abstractions",
    hue: 321,
  },
  {
    id: "backend",
    label: "Backend",
    tagline: "Production-grade endpoints and failure handling",
    hue: 20,
  },
  {
    id: "system-design",
    label: "System design",
    tagline: "Design choices for growth, latency, and reliability",
    hue: 49,
  },
  {
    id: "devops",
    label: "DevOps",
    tagline: "CI/CD discipline and operational excellence",
    hue: 116,
  },
  {
    id: "dbms",
    label: "Databases",
    tagline: "Queries, indexes, transactions, data correctness",
    hue: 68,
  },
];

export const MODULE_IDS = MODULE_CATALOG.map((m) => m.id);

export function moduleMeta(id: string): ModuleMeta | undefined {
  return MODULE_CATALOG.find((m) => m.id === id);
}
