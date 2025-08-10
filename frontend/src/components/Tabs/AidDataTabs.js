import { useEffect, useState } from "react";
import { Textarea, Box, Text } from "@chakra-ui/react";
import { SelectChoice } from "../choice.field";
import { AID_EFFECTS } from "../../constants/select-text";

const AidDataTabs = ({ aid, onSaveRef }) => {
  const [localData, setLocalData] = useState(aid);

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
