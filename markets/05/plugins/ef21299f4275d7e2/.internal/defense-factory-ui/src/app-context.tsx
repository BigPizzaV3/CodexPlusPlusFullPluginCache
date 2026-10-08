import { createContext, useContext } from "react";
import type { DefenseFactoryBootstrap } from "./contract";

export const CloudContext = createContext<DefenseFactoryBootstrap | null>(null);

export function useCloud(): DefenseFactoryBootstrap {
  const cloud = useContext(CloudContext);
  if (!cloud) throw new Error("Security has not connected to its host");
  return cloud;
}
