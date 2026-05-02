import { useEffect, useRef } from "react";
import * as THREE from "three";

/** Subtle 3D grid + floating bits — stays behind UI */
export function DigitalBackground() {
  const mountRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const mount = mountRef.current;
    if (!mount) return;

    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x030510, 0.035);

    const camera = new THREE.PerspectiveCamera(
      55,
      mount.clientWidth / Math.max(mount.clientHeight, 1),
      0.1,
      120,
    );
    camera.position.set(0, 2.2, 9);

    const renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
      powerPreference: "high-performance",
    });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(mount.clientWidth, mount.clientHeight);
    renderer.setClearColor(0x000000, 0);
    mount.appendChild(renderer.domElement);

    const grid = new THREE.GridHelper(40, 40, 0x22d3ee, 0x1e1b4b);
    grid.position.y = -1.6;
    grid.material.opacity = 0.35;
    (grid.material as THREE.Material).transparent = true;
    scene.add(grid);

    const planeGeo = new THREE.PlaneGeometry(24, 14, 18, 10);
    const pos = planeGeo.attributes.position as THREE.BufferAttribute;
    for (let i = 0; i < pos.count; i++) {
      const x = pos.getX(i);
      const y = pos.getY(i);
      const w = Math.sin(x * 0.5) * 0.35 + Math.cos(y * 0.7) * 0.25;
      pos.setZ(i, w);
    }
    planeGeo.computeVertexNormals();
    const planeMat = new THREE.MeshStandardMaterial({
      color: 0x0a1628,
      emissive: 0x0c4a6e,
      emissiveIntensity: 0.25,
      metalness: 0.85,
      roughness: 0.35,
      side: THREE.DoubleSide,
      transparent: true,
      opacity: 0.92,
    });
    const plane = new THREE.Mesh(planeGeo, planeMat);
    plane.rotation.x = -Math.PI / 2.15;
    plane.position.y = -1.45;
    scene.add(plane);

    const ambient = new THREE.AmbientLight(0x6b21a8, 0.35);
    scene.add(ambient);
    const key = new THREE.DirectionalLight(0x22d3ee, 1.1);
    key.position.set(6, 10, 8);
    scene.add(key);
    const rim = new THREE.PointLight(0xf472b6, 0.9, 30);
    rim.position.set(-8, 4, -2);
    scene.add(rim);

    const bitsGeo = new THREE.BufferGeometry();
    const n = 900;
    const positions = new Float32Array(n * 3);
    for (let i = 0; i < n; i++) {
      positions[i * 3] = (Math.random() - 0.5) * 28;
      positions[i * 3 + 1] = Math.random() * 8 - 0.5;
      positions[i * 3 + 2] = (Math.random() - 0.5) * 18;
    }
    bitsGeo.setAttribute("position", new THREE.BufferAttribute(positions, 3));
    const bitsMat = new THREE.PointsMaterial({
      color: 0x67e8f9,
      size: 0.045,
      transparent: true,
      opacity: 0.55,
      depthWrite: false,
      blending: THREE.AdditiveBlending,
    });
    const bits = new THREE.Points(bitsGeo, bitsMat);
    scene.add(bits);

    let raf = 0;
    const t0 = performance.now();
    const tick = (now: number) => {
      const t = (now - t0) * 0.001;
      grid.rotation.y = t * 0.06;
      plane.rotation.z = Math.sin(t * 0.2) * 0.04;
      bits.rotation.y = t * 0.03;
      camera.position.x = Math.sin(t * 0.12) * 0.6;
      camera.lookAt(0, -0.2, 0);
      renderer.render(scene, camera);
      raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);

    const ro = new ResizeObserver(() => {
      if (!mount) return;
      const w = mount.clientWidth;
      const h = Math.max(mount.clientHeight, 1);
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    });
    ro.observe(mount);

    return () => {
      cancelAnimationFrame(raf);
      ro.disconnect();
      renderer.dispose();
      planeGeo.dispose();
      planeMat.dispose();
      bitsGeo.dispose();
      bitsMat.dispose();
      grid.geometry.dispose();
      const gm = grid.material;
      if (Array.isArray(gm)) gm.forEach((m) => m.dispose());
      else gm.dispose();
      mount.removeChild(renderer.domElement);
    };
  }, []);

  return (
    <div
      ref={mountRef}
      className="digital-bg"
      aria-hidden
    />
  );
}
