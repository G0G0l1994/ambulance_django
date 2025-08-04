import { Grid, GridItem, HStack, Input, Text } from "@chakra-ui/react";
import { useEffect, useState } from "react";

import { SelectChoice } from "./choice.field";
import {
  SKIN_COLOR_CHOICES,
  SKIN_DRYNESS_CHOICES,
  RASH_CHOICES,
  SWELLING_CHOICES,
  THROAT_CHOICES,
} from "../constants/select-text";

const SkinTabs = ({ skin, onRefSave }) => {
  const [localData, setLocalData] = useState(skin);

  const handleChange = (field, value) => {
    setLocalData((prev) => ({
      ...prev,
      [field]: value,
    }));
  };

  useEffect(() => {
    if (onRefSave) {
      onRefSave.current = () => localData;
    }
  }, [localData, onRefSave]);

  return (
    <Grid gap={6} templateColumns="repeat(2, 1fr)">
      <GridItem columnGap={6}>
        <SelectChoice
          fieldname="Кожные покровы"
          options={SKIN_COLOR_CHOICES}
          defaultValue={localData.color_skin}
          onChange={(e) => {
            handleChange("color_skin", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Влажность"
          options={SKIN_DRYNESS_CHOICES}
          defaultValue={localData.dry_skin}
          onChange={(e) => {
            handleChange("dry_skin", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Сыпь"
          options={RASH_CHOICES}
          defaultValue={localData.rash}
          onChange={(e) => {
            handleChange("rash", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Отеки"
          options={SWELLING_CHOICES}
          defaultValue={localData.swelling}
          onChange={(e) => {
            handleChange("swelling", e.target.value);
          }}
        />
      </GridItem>
      <GridItem columnGap={6}>
        <SelectChoice
          fieldname="Зев"
          options={THROAT_CHOICES}
          defaultValue={localData.throat}
          onChange={(e) => {
            handleChange("throat", e.target.value);
          }}
        />
        <HStack>
          <Text>Миндалины</Text>
          <Input
            value={localData.tonsils}
            onChange={(e) => {
              handleChange("tonsils", e.target.value);
            }}
          />
        </HStack>
        <HStack>
          <Text>Лимфатические узлы</Text>
          <Input
            value={localData.lymph_nodes}
            onChange={(e) => {
              handleChange("lymph_nodes", e.target.value);
            }}
          />
        </HStack>
        <HStack>
          <Text>Желтушность</Text>
          <Input
            value={localData.jaundice}
            onChange={(e) => {
              handleChange("jaundice", e.target.value);
            }}
          />
        </HStack>
      </GridItem>
    </Grid>
  );
};

export default SkinTabs;
