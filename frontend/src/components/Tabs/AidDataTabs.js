import { useEffect, useState, useCallback } from "react";
import { Textarea, Box, Text } from "@chakra-ui/react";
import { SelectChoice } from "../fields/choice.field";
import { AID_EFFECTS } from "../../constants/select-text";
import { debounce } from "lodash";

const AidDataTabs = ({ aid_data, onRefSave }) => {
  const [localData, setLocalData] = useState(aid_data || {});

  // Обновляем localData при изменении пропсов
  useEffect(() => {
    if (aid_data) {
      setLocalData(aid_data);
    }
  }, [aid_data]);

  const handleChange = (field, value) => {
    setLocalData((prev) => ({
      ...prev,
      [field]: value,
    }));
  };

  useEffect(() => {
    if (onRefSave) {
      onRefSave.current = () => localData || {};
    }
  }, [localData, onRefSave]);

  return (
    <Box>
      <Text>Оказание помощи:</Text>
      <Textarea
        height="200px"
        value={localData.aid}
        onChange={(e) => {
          handleChange("aid", e.target.value);
        }}
      />
      <SelectChoice
        fieldname="Эффект помощи"
        options={AID_EFFECTS}
        defaultValue={localData.aid_effect}
        onChange={(e) => {
          handleChange("aid_effect", e.target.value);
        }}
      />
    </Box>
  );
};

export default AidDataTabs;
