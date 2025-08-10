import { useEffect, useState } from "react";

import { Box, Textarea, Input, Text, HStack } from "@chakra-ui/react";

const DiagnosisDataTabs = ({ diagnosis, onSaveRef }) => {
  const [localData, setLocalData] = useState(diagnosis);

  const handleChange = (field, value) => {
    setLocalData((prev) => ({ ...prev, [field]: value }));
  };

  useEffect(() => {
    if (onSaveRef) {
      onSaveRef.current = () => localData;
    }
  }, [localData, onSaveRef]);

  return (
    <Box>
      <HStack>
        <Text>Предварительный диагноз:</Text>
        <Textarea
          value={localData.diagnosis}
          onChange={(e) => {
            handleChange("diagnosis", e.target.value);
          }}
        />
      </HStack>
      <HStack gap="95px">
        <Text>Код МКБ-10</Text>
        <Input
          value={localData.mkb}
          onChange={(e) => {
            handleChange("mkb", e.target.value);
          }}
        />
      </HStack>
    </Box>
  );
};

export default DiagnosisDataTabs;
