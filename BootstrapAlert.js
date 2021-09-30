function bootstrapAlert(content="Ok", iconId="check-circle-fill", ariaLabel="Success", alertType="success", alertGroupId="alertGroup") {
  let alertHTML = `<svg
  class="bi flex-shrink-0 me-2"
  width="24"
  height="24"
  role="img"
  aria-label="${ariaLabel}:"
>
  <use xlink:href="#${iconId}" />
</svg>
<div>
	${content}
</div>
<button
  type="button"
  class="btn-close"
  data-bs-dismiss="alert"
  aria-label="Close"
></button>`;

  let alertGroup = document.getElementsByClassName(alertGroupId)[0];
  let alertDiv = document.createElement("div");
  alertDiv.className = `alert alert-dismissible alert-${alertType} d-flex text-center align-items-center fade show`;
  alertDiv.style.textAlign = "center";
  alertDiv.innerHTML = alertHTML;
  alertGroup.appendChild(alertDiv);
  console.error(alertGroupId)
  console.log(alertHTML, alertDiv);
}
