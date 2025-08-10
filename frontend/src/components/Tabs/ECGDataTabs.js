import { useEffect, useState } from "react";

import { Grid, GridItem, Textarea, Text, Select } from "@chakra-ui/react";

const ECGDataTabs = ({ ecg, onRefSave }) => {
  const [localData, setLocalData] = useState(ecg);

  const handleChange = (field, value) => {
    setLocalData((prev) => ({ ...prev, [field]: value }));
  };

  useEffect(() => {
    if (onRefSave) {
      onRefSave.current = () => localData;
    }
  }, [localData, onRefSave]);

  return (
    <Grid templateColumns="repeat(2,1fr)" gap={6}>
      <GridItem gap={6}>
        <Text>Экг до оказания помощи:</Text>
        <Textarea
          p="20px"
          height="200px"
          value={localData.ecg_before}
          onChange={(e) => {
            handleChange("ecg_before", e.target.value);
          }}
        />
      </GridItem>
      <GridItem gap={6}>
        <Text>Экг после оказания помощи:</Text>
        <Textarea
          p="20px"
          height="200px"
          value={localData.ecg_after}
          onChange={(e) => {
            handleChange("ecg_after", e.target.value);
          }}
        />
      </GridItem>
    </Grid>
  );
};

export default ECGDataTabs;
