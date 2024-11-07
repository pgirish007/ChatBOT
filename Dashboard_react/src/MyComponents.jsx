// Import necessary libraries
import { render } from "solid-js/web";
import { createSignal } from "solid-js";
import { reactify } from "solid-react-compat";
import { Button, Label, ListBox, ListBoxItem, Popover, Select, SelectValue } from "react-aria-components";

// Wrap the React component using solid-react-compat
const SolidReactSelect = reactify(Select);

function MySolidComponent() {
  const [selectedAnimal, setSelectedAnimal] = createSignal("Cat");

  return (
    <SolidReactSelect>
      <Label>Favorite Animal</Label>
      <Button>
        <SelectValue />
        <span aria-hidden="true">▼</span>
      </Button>
      <Popover>
        <ListBox>
          <ListBoxItem onClick={() => setSelectedAnimal("Cat")}>Cat</ListBoxItem>
          <ListBoxItem onClick={() => setSelectedAnimal("Dog")}>Dog</ListBoxItem>
          <ListBoxItem onClick={() => setSelectedAnimal("Kangaroo")}>Kangaroo</ListBoxItem>
        </ListBox>
      </Popover>
    </SolidReactSelect>
  );
}

render(() => <MySolidComponent />, document.getElementById("root"));
