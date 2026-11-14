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
    hue: 331,
  },
  {
    id: "frontend-basics",
    label: "Frontend foundations",
    tagline: "UI structure, accessibility, and rendering speed",
    hue: 120,
  },
  {
    id: "javascript-typescript",
    label: "JavaScript & TypeScript",
    tagline: "Runtime safety with practical TypeScript patterns",
    hue: 168,
  },
  {
    id: "backend",
    label: "Backend",
    tagline: "APIs, auth, reliability, and service boundaries",
    hue: 187,
  },
  {
    id: "system-design",
    label: "System design",
    tagline: "Scale, tradeoffs, and architecture judgement",
    hue: 216,
  },
  {
    id: "devops",
    label: "DevOps",
    tagline: "CI/CD discipline and operational excellence",
    hue: 283,
  },
  {
    id: "dbms",
    label: "Databases",
    tagline: "Storage design and performance tuning fundamentals",
    hue: 235,
  },
];

export const MODULE_IDS = MODULE_CATALOG.map((m) => m.id);

export function moduleMeta(id: string): ModuleMeta | undefined {
  return MODULE_CATALOG.find((m) => m.id === id);
}
