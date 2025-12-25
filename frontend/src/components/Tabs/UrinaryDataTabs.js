import { useEffect, useState } from "react";
import { Grid, GridItem, HStack, Text, Checkbox, Box } from "@chakra-ui/react";
import { SelectChoice } from "../fields/choice.field";
import {
  PAINLESS_URINATION_CHOICES,
  CHARACTERISTIC_URINATION_CHOICES,
  KIDNEY_PUNCH_CHOICES,
  CHARACTERISTIC_URINE_CHOICES,
} from "../../constants/select-text";

const UrinaryDataTabs = ({ urinary, onRefSave }) => {
  const [localData, setLocalData] = useState(urinary || {});

  // Обновляем localData при изменении пропсов
  useEffect(() => {
    if (urinary) {
      setLocalData(urinary);
    }
  }, [urinary]);

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
      <Grid templateColumns="repeat(2,1fr)">
        <GridItem gap={6}>
          <SelectChoice
            fieldname="Болезненность мочеиспускания"
            options={PAINLESS_URINATION_CHOICES}
            defaultValue={localData.painless_urination}
            onChange={(e) => {
              handleChange("painless_urination", e.target.value);
            }}
          />
          <SelectChoice
            fieldname="Характеристика мочеиспускания"
            options={CHARACTERISTIC_URINATION_CHOICES}
            defaultValue={localData.characteristic_urination}
            onChange={(e) => {
              handleChange("characteristic_urination", e.target.value);
            }}
          />
        </GridItem>
        <GridItem gap={6}>
          <SelectChoice
            fieldname="Моча"
            options={CHARACTERISTIC_URINE_CHOICES}
            defaultValue={localData.characteristic_urine}
            onChange={(e) => {
              handleChange("characteristic_urine", e.target.value);
            }}
          />
          <HStack>
            <Checkbox
              p="10px"
              pt="20px"
              isChecked={localData.with_inclusions}
              onChange={(e) => {
                handleChange("with_inclusions", e.target.checked);
              }}
            >
              С включениями
            </Checkbox>
            <Checkbox
              p="10px"
              pt="20px"
              isChecked={localData.with_sediment}
              onChange={(e) => {
                handleChange("with_sediment", e.target.checked);
              }}
            >
              С осадком
            </Checkbox>
          </HStack>
        </GridItem>
      </Grid>
      <SelectChoice
        fieldname="Симптом поколачивания"
        options={KIDNEY_PUNCH_CHOICES}
        defaultValue={localData.kidney_punch}
        onChange={(e) => {
          handleChange("kidney_punch", e.target.value);
        }}
      />
    </Box>
  );
};

export default UrinaryDataTabs;
