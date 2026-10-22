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
    hue: 255,
  },
  {
    id: "frontend-basics",
    label: "Frontend foundations",
    tagline: "UI structure, accessibility, and rendering speed",
    hue: 303,
  },
  {
    id: "javascript-typescript",
    label: "JavaScript & TypeScript",
    tagline: "Runtime safety with practical TypeScript patterns",
    hue: 31,
  },
  {
    id: "backend",
    label: "Backend",
    tagline: "APIs, auth, reliability, and service boundaries",
    hue: 50,
  },
  {
    id: "system-design",
    label: "System design",
    tagline: "Design choices for growth, latency, and reliability",
    hue: 79,
  },
  {
    id: "devops",
    label: "DevOps",
    tagline: "Build, release, observe, and recover confidently",
    hue: 207,
  },
  {
    id: "dbms",
    label: "Databases",
    tagline: "Storage design and performance tuning fundamentals",
    hue: 98,
  },
];

export const MODULE_IDS = MODULE_CATALOG.map((m) => m.id);

export function moduleMeta(id: string): ModuleMeta | undefined {
  return MODULE_CATALOG.find((m) => m.id === id);
}
