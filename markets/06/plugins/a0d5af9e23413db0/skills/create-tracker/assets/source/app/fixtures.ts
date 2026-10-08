export type FloorId = "first";
export type SystemId = "power";
export type Fixture = {
  id: string;
  type: string;
  subject: string;
  floor: FloorId;
  system: SystemId;
  x: number;
  y: number;
};

// Replace this sample plan and device list with data extracted from the
// new project's unflattened Bluebeam Count markups before publishing.
export const planImages: Record<SystemId, Record<FloorId, { label: string; image: string }>> = {
  power: {
    first: { label: "First Floor", image: "/sample-plan.svg" },
  },
};

export const fixtures: Fixture[] = [
  {
    id: "SAMPLE-DEVICE-01",
    type: "Sample Device",
    subject: "Sample Device",
    floor: "first",
    system: "power",
    x: 50,
    y: 50,
  },
];
