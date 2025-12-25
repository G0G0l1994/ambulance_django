import { useState, useEffect, useCallback } from "react";
import { HStack, Input, Text, Grid, GridItem } from "@chakra-ui/react";
import debounce from "lodash/debounce";
import { SelectChoice } from "../fields/choice.field";

import {
  RESPIRATORY_TYPE_CHOICES,
  WHEEZING_CHOICES,
  DYSPNEA_CHOICES,
} from "../../constants/select-text";

const AirDataTabs = ({ air, onRefSave }) => {
  const [localData, setLocalData] = useState(air || {});

  // Обновляем localData при изменении пропсов
  useEffect(() => {
    if (air) {
      setLocalData(air);
    }
  }, [air]);

  const debounceUpdate = useCallback(
    debounce((newData) => {
      setLocalData(newData);
    }, 500),
    []
  );

  const handleChange = (field, value) => {
    setLocalData((prev) => {
      const newData = { ...prev, [field]: value };
      debounceUpdate(newData);
      return newData;
    });
  };
  useEffect(() => {
    debounceUpdate.cancel();
  }, []);
  useEffect(() => {
    if (onRefSave) {
      onRefSave.current = () => localData || {};
    }
  }, [localData, onRefSave]);

  return (
    <Grid gap={6} templateColumns="repeat(2, 1fr)">
      <GridItem columnGap={6}>
        <SelectChoice
          fieldname="Тип дыхания"
          options={RESPIRATORY_TYPE_CHOICES}
          defaultValue={localData.respiratory_type}
          onChange={(e) => {
            handleChange("respiratory_type", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Хрипы"
          options={WHEEZING_CHOICES}
          defaultValue={localData.wheezing}
          onChange={(e) => {
            handleChange("wheezing", e.target.value);
          }}
        />
      </GridItem>
      <GridItem columnGap={6}>
        <SelectChoice
          fieldname="Одышка"
          options={DYSPNEA_CHOICES}
          defaultValue={localData.dyspnea}
          onChange={(e) => {
            handleChange("dyspnea", e.target.value);
          }}
        />
        <HStack p={2}>
          <Text>Локализация хрипов</Text>
          <Input
            value={localData.wheezing_localisation}
            onChange={(e) => {
              handleChange("wheezing_localisation", e.target.value);
            }}
          />
        </HStack>
      </GridItem>
    </Grid>
  );
};

export default AirDataTabs;
